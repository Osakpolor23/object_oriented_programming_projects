from fpdf import FPDF

class Shirtificate(FPDF):
    def __init__(self, name):
        # Accessing the parent class constructor using super() 
        super().__init__(orientation="P", format="A4") # initializing the PDF with portrait orientation and A4 size
        self.add_page()
        self.set_font("Helvetica", size=32)
        # Set the title 
        self.cell(0, 10, "CS50 Shirtificate", align="C") 
        # Set the image path and position
        self.image("shirtificate.png", x=10, y=30, w=190)
        # Set the text color to white
        self.set_text_color(255, 255, 255)
        # Set the position for the text
        text_width = self.get_string_width(f"{name} took CS50")
        # Center the text horizontally
        self.text((210 - text_width) / 2, 100, f"{name} took CS50")
        


def main():
    name = input("Enter your name: ")
    # Create an instance of Shirtificate with the provided name
    shirtificate = Shirtificate(name)
    # Output the shirtificate to a PDF file
    shirtificate.output("shirtificate.pdf")
    print(f"Shirtificate for {name} created successfully!")


if __name__ == "__main__":
    main()


# Download the shirtificate image from the CS50 website using the following command:
# wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png
