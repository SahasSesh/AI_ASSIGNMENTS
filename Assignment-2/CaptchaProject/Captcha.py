import random
import string
import os

try:
    from captcha.image import ImageCaptcha
    HAS_CAPTCHA_LIB = True
except ImportError:
    HAS_CAPTCHA_LIB = False


def generate_math_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        if num1 < num2:
            num1, num2 = num2, num1
        answer = num1 - num2
    else:
        answer = num1 * num2

    question = f"What is {num1} {operator} {num2}?"
    return question, str(answer)


def generate_text_string(length=6):
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(characters) for _ in range(length))
    return captcha_text


def generate_image_captcha(text=None, filename="captcha.png", output_dir="."):
    if not HAS_CAPTCHA_LIB:
        print("Install captcha library: pip install captcha")
        return None, None

    if text is None:
        text = generate_text_string()

    image = ImageCaptcha(width=280, height=90)

    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)

    image.write(text, filepath)
    print(f"Captcha saved as: {filepath}")

    return text, filepath


if __name__ == "__main__":

    question, correct_answer = generate_math_captcha()
    print(question)

    user_input = input("Enter your answer: ")

    if user_input.strip() == correct_answer:
        print("Correct")
    else:
        print("Wrong")

    if HAS_CAPTCHA_LIB:
        expected_text, img_file = generate_image_captcha()
        print(f"Open {img_file} to see captcha")

        user_input = input("Enter captcha text: ")

        if user_input.strip() == expected_text:
            print("Captcha solved")
        else:
            print("Captcha incorrect")
