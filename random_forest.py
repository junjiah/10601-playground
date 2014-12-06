import sys

from sklearn.ensemble import RandomForestClassifier

from sklearn.externals import joblib

from classifier import MyClassifier

from util import load_pickled_dataset


__author__ = 'junjiah'


class MyRandomForest(MyClassifier):
    def __init__(self):
        self.random_forest = None

    def train(self, n_estimators=20, n_jobs=8):
        labels, instances = load_pickled_dataset('data/train.pkl')

        self.random_forest = RandomForestClassifier(n_estimators=n_estimators, n_jobs=n_jobs,
                                                    verbose=2)
        self.random_forest.fit(instances, labels)

        print "STATUS: model training done. "
        print "INFO: " + str(self.random_forest)

    def predict(self):
        labels, instances = load_pickled_dataset('data/test.pkl')
        return self.random_forest.predict(instances)

    def save(self, file_path='model/rf_model'):
        joblib.dump(self.random_forest, file_path)

    def load(self, file_path='model/rf_model'):
        self.random_forest = joblib.load(file_path)

    def write_results(self, predictions):
        super(MyRandomForest, self).write(predictions, 'rf_prediction.csv')


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'train':
        RF = MyRandomForest()
        RF.train()
    else:
        print 'INFO: so you just wanna load some functions? ok...'