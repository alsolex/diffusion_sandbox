import os
import json

from urllib.request import urlretrieve


def load_imgs(url: str, imgs_path: str) -> None:
    dates_buf, _ = urlretrieve(f"{url}/api/images.php?available_dates")

    with open(dates_buf, encoding="utf-8") as html:
        dates = json.loads(html.read())

    fns = set(os.listdir(imgs_path))
    for date in dates:
        cur_url = f"{url}/api/images.php?date={date}"
        temp_data, _ = urlretrieve(cur_url)

        with open(temp_data) as data_buf:
            data = json.loads(data_buf.read())

        for img_meta in data:
            fn = f"{img_meta['image']}.jpg"
            if fn in fns:
                continue
            fns.add(fn)
            urlretrieve(f"{url}/epic-archive/jpg/{fn}", f"{imgs_path}/{fn}")
