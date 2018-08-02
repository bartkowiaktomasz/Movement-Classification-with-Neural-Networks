##################################################
### GLOBAL VARIABLES
##################################################
COLUMN_NAMES = [
    'activity',
    'acc-x-axis',
    'acc-y-axis',
    'acc-z-axis',
    'gyro-x-axis',
    'gyro-y-axis',
    'gyro-z-axis',
    'mag-x-axis',
    'mag-y-axis',
    'mag-z-axis'
]

LABELS_NAMES = [
    'Pushup',
    'Pushup_Incorrect',
    'Squat',
    'Situp',
    'Situp_Incorrect',
    'Jumping',
    'Lunge'
]

# Data
DATA_DIR = 'data/'
DATA_TEMP_DIR = 'web_app/data_temp/'
DATA_PATH = 'data/data.pckl'

# Model
MODEL_PATH = 'models/model.h5'
MODEL_PATH_DIR = 'models/'

# Tensorflow only
MODEL_META_PATH = 'models/model.ckpt.meta'


##################################################
### MODEL
##################################################
RANDOM_SEED = 13

# Model
N_CLASSES = len(LABELS_NAMES)
N_FEATURES = 9  # acc, gyro, magnetometer

# Hyperparameters
N_LSTM_LAYERS = 2
N_EPOCHS = 30
LEARNING_RATE = 0.0005
N_HIDDEN_NEURONS = 30
BATCH_SIZE = 30
DROPOUT_RATE = 0.2

##################################################
### DATA COLLECTION/PREPROCESSING
##################################################
IMU_MAC_ADDRESS = "FF:3C:8F:22:C9:C8"
UUID_DATA = "2d30c082-f39f-4ce6-923f-3484ea480596"
BLE_HANDLE = "0x0011"

BLE_DATA_COLLECTION_LATENCY = 0.35

# Data type sent from the device
DATA_TYPE = 'h' # Short integer
DATA_SIZE_BYTES = 2 # Size of short

# How many times to collect samples
DATA_COLLECTION_TIME = 80
SCALE_FACTOR = 100

# Data preprocessing
TIME_STEP = 5
SEGMENT_TIME_SIZE = 40

# Train/test proportion
TEST_SIZE = 0.2

##################################################
### VISUALIZE
##################################################
plotRange_x = 50
plotRange_y = 20

##################################################
### BACKEND REQUEST
##################################################
PROTOCOL = "http://"
PORT = ":5000"
IP_ADDRESS = PROTOCOL + "104.40.158.95" + PORT
IP_LOCAL = "http://192.168.1.71:5000"
PAYLOAD_KEY = "payload_json"
