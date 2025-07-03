# Digit Recognition App

A simple digit recognition application built using Python, Pygame, and Keras.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-username/digit-recognition-app.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Run the `prjct.py` script:
```
python prjct.py
```
2. The application window will open, allowing you to draw a digit on the screen.
3. The recognized digit will be displayed in the top-left corner of the window.
4. Press the 'n' key to clear the drawing area.

## API

The application uses the following APIs and libraries:

- **Pygame**: For creating the drawing canvas and handling user input.
- **Keras**: For loading the pre-trained digit recognition model and making predictions.
- **OpenCV (cv2)**: For image processing and saving the drawn digit.
- **NumPy**: For array manipulation and image preprocessing.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

To run the tests for this project, use the following command:

```
python -m unittest discover tests/
```

This will run all the test cases located in the `tests/` directory.
