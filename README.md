# trellis-challenge
This is a simple Django (Ninja) Vue web app for converting numbers into English.

## Setting up:
1. Clone this repository.
2. Create a virtual environment:
   1. Run `python -m venv .venv` in the root directory to create a virtual environment.
3. Start the virtual environment:
   1. Run `source .venv/bin/activate` (Mac) or `.venv\Scripts\Activate.ps1` (Windows Powershell) to start the virtual environment.
4. Install the requirements:
   1. Run `pip install -r requirements.txt` to install the requirements.
5. Run migrations:
   1. `python -m manage migrate`
6. Install node modules:
   1. Go to the client folder and run `npm install`.

## Running the applications:
1. Start the backend server:
   1. Run `python -m manage runserver` in the root.
2. Start the frontend server:
   1. cd to the `client` folder and run `npm run dev`
3. The application should be available at http://localhost:5173/test/. 

## Running tests:
1. In the root, run `python -m pytest numstowords/tests/` to run the tests for the 
`convert_num_to_english` function. 