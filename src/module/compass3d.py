####################################################################################
# Compass3D - класс взаимодействия с CAD Компас 3Д
####################################################################################
import pythoncom
from win32com.client import Dispatch, gencache

import src.module.compassfile.LDefin2D as LD2D
import src.module.compassfile.MiscellaneousHelpers as MH
from src.module.point2d import Point2D


class Compass3D:

    def __init__(self):
        #  Подключим константы API Компас
        self.kompas6_constants = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
        self.kompas6_constants_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

        #  Подключим описание интерфейсов API5
        self.kompas6_api5_module = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
        self.kompas_object = self.kompas6_api5_module.KompasObject(
            Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(self.kompas6_api5_module.KompasObject.CLSID,
                                                                     pythoncom.IID_IDispatch))
        MH.iKompasObject = self.kompas_object

        #  Подключим описание интерфейсов API7
        self.kompas_api7_module = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)

        self.application = self.kompas_api7_module.IApplication(
            Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(self.kompas_api7_module.IApplication.CLSID,
                                                                     pythoncom.IID_IDispatch))
        MH.iApplication = self.application

        self.Documents = self.application.Documents
        #  Получим активный документ
        self.kompas_document = self.application.ActiveDocument
        self.kompas_document_2d = self.kompas_api7_module.IKompasDocument2D(self.kompas_document)
        self.iDocument2D = self.kompas_object.ActiveDocument2D()
        self.obj = 0

        # переменные для вывода текста на чертеж
        self.iParagraphParam = 0
        self.iTextLineParam = 0
        self.iTextItemFont = 0
        self.iTextItemArray = 0
        self.iTextItemParam = 0

        # рисование линии по координатам точек
    def draw_line(self, pt1, pt2):
        self.obj = self.iDocument2D.ksLineSeg(pt1.x, pt1.y, pt2.x, pt2.y, 1)

    # рисование окружности по координате центра и радиусу
    def draw_circle(self, pt, radius):
        self.obj = self.iDocument2D.ksCircle(pt.x, pt.y, radius, 1)

    # рисование объкта из прямых линий по координатам из массива точек
    def draw_object(self, pt_array):
        if len(pt_array) < 2:
            raise Exception("Координат точек должно быть миниму 2")
        for i in range(0, len(pt_array)-1):     # количество отрезков меньше на 1, чем точек
            self.obj = self.iDocument2D.ksLineSeg(pt_array[i].x, pt_array[i].y,
                                                  pt_array[i+1].x, pt_array[i+1].y, 1)

    # рисование прямоугольника по координатам противоположных вершин
    def draw_rectangle(self, pt1, pt2):
        # нижняя горизонтальная
        self.obj = self.iDocument2D.ksLineSeg(pt1.x, pt1.y, pt2.x, pt1.y, 1)
        # верхняя горизонтальная
        self.obj = self.iDocument2D.ksLineSeg(pt1.x, pt2.y, pt2.x, pt2.y, 1)
        # левая вертикальная
        self.obj = self.iDocument2D.ksLineSeg(pt1.x, pt1.y, pt1.x, pt2.y, 1)
        # правая вертикальная
        self.obj = self.iDocument2D.ksLineSeg(pt2.x, pt1.y, pt2.x, pt2.y, 1)

    # Вывод теста text с начальными координатами pt
    def draw_text(self, pt,  text):
        self.iParagraphParam = self.kompas6_api5_module.ksParagraphParam(
            self.kompas_object.GetParamStruct(self.kompas6_constants.ko_ParagraphParam))
        self.iParagraphParam.Init()
        self.iParagraphParam.x = pt.x
        self.iParagraphParam.y = pt.y
        self.iParagraphParam.ang = 0
        self.iParagraphParam.height = 19.980276107788
        self.iParagraphParam.width = 68.066825866699
        self.iParagraphParam.hFormat = 0
        self.iParagraphParam.vFormat = 0
        self.iParagraphParam.style = 1
        self.iDocument2D.ksParagraph(self.iParagraphParam)

        self.iTextLineParam = self.kompas6_api5_module.ksTextLineParam(
            self.kompas_object.GetParamStruct(self.kompas6_constants.ko_TextLineParam))
        self.iTextLineParam.Init()
        self.iTextLineParam.style = 1
        self.iTextItemArray = self.kompas_object.GetDynamicArray(LD2D.TEXT_ITEM_ARR)
        self.iTextItemParam = self.kompas6_api5_module.ksTextItemParam(
            self.kompas_object.GetParamStruct(self.kompas6_constants.ko_TextItemParam))
        self.iTextItemParam.Init()
        self.iTextItemParam.iSNumb = 0
        self.iTextItemParam.s = text
        self.iTextItemParam.type = 0
        self.iTextItemFont = self.kompas6_api5_module.ksTextItemFont(self.iTextItemParam.GetItemFont())
        self.iTextItemFont.Init()
        self.iTextItemFont.bitVector = 4096
        self.iTextItemFont.color = 0
        self.iTextItemFont.fontName = "GOST type A"
        self.iTextItemFont.height = 14
        self.iTextItemFont.ksu = 1
        self.iTextItemArray.ksAddArrayItem(-1, self.iTextItemParam)
        self.iTextLineParam.SetTextItemArr(self.iTextItemArray)

        self.iDocument2D.ksTextLine(self.iTextLineParam)
        self.obj = self.iDocument2D.ksEndObj()


if __name__ == '__main__':

    # тестовые объкты точек
    pt1 = Point2D(10, 10)
    pt2 = Point2D(100, 100)

    # тестовый  массив точек
    pt = [Point2D(-10, -10), Point2D(-100, -100), Point2D(100, 200), Point2D(300, 100), Point2D(400, 400)]
    pt.append(Point2D(-400, 300))    # добавить еще одну координату

    s = Compass3D()

    s.draw_line(pt1, pt2)
    s.draw_circle(pt1, 200)
    s.draw_rectangle(pt1, pt2)
    s.draw_object(pt)
    s.draw_text(pt1,  "Привет, МИР!!!!")




