from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 32)
        self.cell(
            96,
            9,
            self.title,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            center=True,
        )
        self.ln(20)
        self.image("shirtificate.png", w =190, h=190)

def main():
    pdf = PDF(orientation="P", format="A4")
    pdf.set_title("CS50 Shirtificate")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    name = input("Your name: ")
    x_position = 60
    y_position = 95
    pdf.set_xy(x_position, y_position)
    pdf.multi_cell(100, 10,  f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()
