URL='http://epic.gsfc.nasa.gov'
IMGS_PATH='./data'

mkdir ${IMGS_PATH}
python3 -c "from utils import load_imgs; load_imgs('${URL}', '${IMGS_PATH}')"

