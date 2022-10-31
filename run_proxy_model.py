
from proxy_model_EDA import ProxyModelEDA

DATASET_FILENAME = 'data.csv'
DATA_DIRECTORY = 'data'

def main():
    # First do some EDA
    eda = ProxyModelEDA(DATASET_FILENAME, 
                  DATA_DIRECTORY)


if __name__ == '__main__':
    main()
