import pandas as pd
from sklearn.feature_selection import mutual_info_classif

train = pd.read_csv("train.csv")


def test_survived_distribution():
    survived = train["Survived"].value_counts(normalize=True)[1]
    assert survived < 0.4


def test_sex_distribution():
    female = train["Sex"].value_counts(normalize=True)["female"]
    assert female < 0.37


def test_class_distribution():
    first_class = train["Pclass"].value_counts(normalize=True)[1]
    assert first_class < 0.26


def test_max_age_less_than_81():
    assert train["Age"].max() < 81


def test_min_age_greater_than_0():
    assert train["Age"].min() > 0


def make_mi_scores(X, y, discrete_features):
    mi_scores = mutual_info_classif(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores


def test_most_important_feature_is_sex():
    train.replace({"Sex": {"male": 0, "female": 1}}, inplace=True)
    train["Age"].fillna(1000, inplace=True)

    X = train[["Pclass", "Sex", "Fare", "Age", "SibSp", "Parch"]]
    y = train["Survived"]

    discrete_features = X.dtypes == int
    mi_scores = make_mi_scores(X, y, discrete_features)

    assert mi_scores.index[0] == "Sex"