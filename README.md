# really bad gif rendering stuff.

Was just curious how this go.

Using `curses` and `Pillow` to render terminals and read images respectively.

Added some `argparse` for some more testing.

## Usage

**Onetime setup**

```
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
```

**Running**

```
> python main.py --file_name="giffo.gif" --wait_time=0.1 --window_width=128 --window_height=64
```

Pretty simple but had fun rendering a gif.

![Example](example.gif)
