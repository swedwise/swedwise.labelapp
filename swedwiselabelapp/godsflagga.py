from reportlab.graphics.barcode import code39
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import random
from config import COLOPHONE, TEMP_FILE_PATH, AUTO_PRINT


class Godsflagga():
    def __init__(self, part_no, quantity,
                 vendor_lot, vendor_number,
                 serial, description, date, po_number):
        self.part_no = part_no
        self.quantity = quantity
        self.vendor_lot = vendor_lot
        self.vendor_number = vendor_number
        self.serial = serial
        self.description = description
        self.date = date
        self.po_number = po_number

    def create(self):
        random_no = random.randint(1000000, 9999999)
        filename = str(random_no) + ".pdf"
        filepath = TEMP_FILE_PATH
        filenamepath = filepath + filename

        if AUTO_PRINT:
            from reportlab.pdfbase import pdfdoc
            pdfdoc.PDFCatalog.OpenAction = '<</S/JavaScript/JS(this.print\({bUI:true,bSilent:false,bShrinkToFit:true}\);)>>'
            pdfdoc.PDFInfo.title = 'Label ' + filename

        c = canvas.Canvas(filenamepath, pagesize=A4)

        # GODSFLAGGA
        x_margin = 2 * mm
        # lines
        c.setLineWidth(1)
        lines = [(3 * mm, 47 * mm + 158 * mm, 206 * mm, 47 * mm + 158 * mm),
                 (143 * mm, 59 * mm + 158 * mm, 206 * mm, 59 * mm + 158 * mm),
                 (3 * mm, 71 * mm + 158 * mm, 206 * mm, 71 * mm + 158 * mm),
                 (3 * mm, 98 * mm + 158 * mm, 206 * mm, 98 * mm + 158 * mm),

                 (143 * mm, 47 * mm + 158 * mm, 143 * mm, 71 * mm + 158 * mm),
                 (114 * mm, 71 * mm + 158 * mm, 114 * mm, 98 * mm + 158 * mm),

                 (3 * mm, 47 * mm, 206 * mm, 47 * mm),
                 (143 * mm, 59 * mm, 206 * mm, 59 * mm),
                 (3 * mm, 71 * mm, 206 * mm, 71 * mm),
                 (3 * mm, 98 * mm, 206 * mm, 98 * mm),

                 (143 * mm, 47 * mm, 143 * mm, 71 * mm),
                 (114 * mm, 71 * mm, 114 * mm, 98 * mm),
                 ]
        c.lines(lines)

        # PARTNO
        # label
        label = "PART NO.(P)"
        c.setFont("Helvetica", 10)

        x = 3 * mm + x_margin
        y = 122 * mm
        c.drawString(x, y, label)
        y = 122 * mm + 158 * mm
        c.drawString(x, y, label)

        # data
        data = self.part_no
        c.setFont("Helvetica-Bold", 50)

        x = 30 * mm
        y = 113 * mm
        c.drawString(x, y, data)
        y = 113 * mm + 158 * mm
        c.drawString(x, y, data)

        # barcode
        barcode = code39.Standard39('P' + data, barWidth=0.50 * mm,
                                    barHeight=12 * mm, checksum=0)

        x = 0 * mm
        y = 100 * mm
        barcode.drawOn(c, x, y)
        y = 100 * mm + 158 * mm
        barcode.drawOn(c, x, y)

        # QUANTITY
        # label
        label = "QUANTITY (Q)"
        c.setFont("Helvetica", 10)

        x = 3 * mm + x_margin
        y = 94 * mm
        c.drawString(x, y, label)
        y = 94 * mm + 158 * mm
        c.drawString(x, y, label)

        # data
        data = self.quantity
        c.setFont("Helvetica-Bold", 48)

        x = 33 * mm
        y = 85 * mm
        c.drawString(x, y, data)
        y = 85 * mm + 158 * mm
        c.drawString(x, y, data)

        # barcode
        barcode = code39.Standard39('Q' + data, barWidth=0.50 * mm,
                                    barHeight=12 * mm, checksum=0)

        x = 0 * mm
        y = 72 * mm
        barcode.drawOn(c, x, y)
        y = 72 * mm + 158 * mm
        barcode.drawOn(c, x, y)

        # VENDOR
        # label
        label = "VENDOR LOT (1T)"
        c.setFont("Helvetica", 10)

        x = 3 * mm + x_margin
        y = 67 * mm
        c.drawString(x, y, label)
        y = 67 * mm + 158 * mm
        c.drawString(x, y, label)

        # data
        data = self.vendor_lot
        c.setFont("Helvetica-Bold", 36)

        x = 41 * mm
        y = 61 * mm
        c.drawString(x, y, data)
        y = 61 * mm + 158 * mm
        c.drawString(x, y, data)

        # barcode
        barcode = code39.Standard39('1T' + data, barWidth=0.50 * mm,
                                    barHeight=12 * mm, checksum=0)

        x = 0 * mm
        y = 48 * mm
        barcode.drawOn(c, x, y)
        y = 48 * mm + 158 * mm
        barcode.drawOn(c, x, y)

        # SERIAL
        # label
        label = "SERIAL (1S)"
        c.setFont("Helvetica", 10)

        x = 3 * mm + x_margin
        y = 43 * mm
        c.drawString(x, y, label)
        y = 43 * mm + 158 * mm
        c.drawString(x, y, label)

        # data
        data = self.vendor_number
        c.setFont("Helvetica-Bold", 32)

        x = 27 * mm
        y = 36 * mm
        c.drawString(x, y, data)
        y = 36 * mm + 158 * mm
        c.drawString(x, y, data)

        # data
        data = '00000' + self.serial
        c.setFont("Helvetica-Bold", 32)

        x = 87 * mm
        y = 36 * mm
        c.drawString(x, y, data)
        y = 36 * mm + 158 * mm
        c.drawString(x, y, data)

        # DESCRIPTION
        # label
        label = "DESCRIPTION"
        c.setFont("Helvetica", 10)

        x = 117 * mm
        y = 94 * mm
        c.drawString(x, y, label)
        y = 94 * mm + 158 * mm
        c.drawString(x, y, label)

        # data
        data = self.description
        c.setFont("Helvetica-Bold", 24)

        x = 118 * mm
        y = 76 * mm
        c.drawString(x, y, data)
        y = 76 * mm + 158 * mm
        c.drawString(x, y, data)

        # DATE
        # label
        label = "MFG DATE"
        c.setFont("Helvetica", 10)

        x = 145 * mm
        y = 67 * mm
        c.drawString(x, y, label)
        y = 67 * mm + 158 * mm
        c.drawString(x, y, label)

        # data
        data = self.date
        c.setFont("Helvetica-Bold", 24)

        x = 145 * mm
        y = 60 * mm
        c.drawString(x, y, data)
        y = 60 * mm + 158 * mm
        c.drawString(x, y, data)

        # PO NUMBER
        # label
        label = "PO NUMBER"
        c.setFont("Helvetica", 10)

        x = 145 * mm
        y = 55 * mm
        c.drawString(x, y, label)
        y = 55 * mm + 158 * mm
        c.drawString(x, y, label)

        # data
        data = self.po_number
        c.setFont("Helvetica-Bold", 24)

        x = 145 * mm
        y = 48 * mm
        c.drawString(x, y, data)
        y = 48 * mm + 158 * mm
        c.drawString(x, y, data)

        # COLOPHONE
        label = COLOPHONE
        c.setFont("Helvetica", 12)
        x = 3 * mm + x_margin
        y = 19 * mm
        c.drawString(x, y, label)
        y = 19 * mm + 158 * mm
        c.drawString(x, y, label)

        c.showPage()
        c.save()
        return {'FILENAME': filename,
                'FILEPATH': filepath,
                'FILENAMEPATH': filenamepath}
