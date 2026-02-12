## Valentine Django App

This is a small Django application that asks:

> Will you be my valentine?

with **Yes** and **No** buttons. The **No** button runs away when you try to hover over or click it, so the user ends up clicking **Yes**.  
On clicking **Yes**, a new page is shown with the message:

> Yesss, thanks for accepting!

and it plays a video named `video_dance.mp4`.

### How to run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Apply migrations:

   ```bash
   python3 manage.py migrate
   ```

3. Place your video file:

   - Put your `video_dance.mp4` file in:
     - `valentine/static/valentine/video_dance.mp4`

4. Start the development server:

   ```bash
   python3 manage.py runserver
   ```

5. Open the app:

   - Go to `http://127.0.0.1:8000/` in your browser.

