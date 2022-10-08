####################################################################################
# Compass3D - класс взаимодействия с CAD Компас 3Д
####################################################################################
import pythoncom
from win32com.client import Dispatch, gencache

import src.module.compassfile.LDefin2D
import src.module.compassfile.MiscellaneousHelpers as MH


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

    # рисование линии по координатам
    def draw_line_coords(self, x1, y1, x2, y2):
        self.obj = 0
        self.obj = self.iDocument2D.ksLineSeg(x1, y1, x2, y2, 1)

    # рисование линии по координатам из массива
    def draw_line(self, line):
        self.obj = 0
        self.obj = self.iDocument2D.ksLineSeg(line[0], line[1], line[2], line[3], 1)

    # рисование окружности по координатам и радиусу
    def draw_circle_coords(self, x, y, r):
        obj = self.iDocument2D.ksCircle(x, y, r, 1)

    # рисование окружности по данным из массива [x, y, radius]
    def draw_circle(self, circle):
        obj = self.iDocument2D.ksCircle(circle[0], circle[1], circle[2], 1)

    # рисование объкта из прямых линий
    def draw_object(self, line_array):
        #self.line_array = line_array
        self.obj = 0
        for i in range(0, len(line_array)):
            self.obj = self.iDocument2D.ksLineSeg(line_array[i][0], line_array[i][1],
                                                  line_array[i][2], line_array[i][3], 1)

    # рисование прямоугольника по координатам
    def draw_rectangle_coords(self, x1, y1, x2,y2):

        # нижняя горизонтальная
        self.obj = self.iDocument2D.ksLineSeg(x1, y1, x2, y1, 1)
        # верхняя горизонтальная
        self.obj = self.iDocument2D.ksLineSeg(x1, y2, x2, y2, 1)
        # левая вертикальная
        self.obj = self.iDocument2D.ksLineSeg(x1, y1, x1, y2, 1)
        # правая вертикальная
        self.obj = self.iDocument2D.ksLineSeg(x2, y1, x2, y2, 1)

    # рисование прямоугольника по массиву точек
    def draw_rectangle(self, line_array):

        # нижняя горизонтальная
        self.obj = self.iDocument2D.ksLineSeg(line_array[0][0], line_array[0][1],
                                              line_array[1][0], line_array[0][1], 1)
        # верхняя горизонтальная
        self.obj = self.iDocument2D.ksLineSeg(line_array[0][0], line_array[1][1],
                                              line_array[1][0], line_array[1][1], 1)

        # левая вертикальная
        self.obj = self.iDocument2D.ksLineSeg(line_array[0][0], line_array[0][1],
                                              line_array[0][0], line_array[1][1], 1)
        # правая вертикальная
        self.obj = self.iDocument2D.ksLineSeg(line_array[1][0], line_array[0][1],
                                              line_array[1][0], line_array[1][1], 1)


    def draw_cottom(self):
        pass


if __name__ == '__main__':
    L = [[10, 10, 100, 100], [100, 100, 400, 150]]
    L1 = [[10, 10], [100, 100], [100, 100], [200, 200]]
    L2 = [0, 0, 120, 350]

    s = Compass3D()
    s.draw_object(L)
    s.draw_rectangle([L1[0], L1[1]])
    s.draw_rectangle([L1[2], L1[3]])
    #s.draw_rectangle(L1)
    s.draw_line(L2)
    s.draw_line_coords(10, 100, 200, -120)
    s.draw_rectangle_coords(50, 50, 400, 400)

    s.draw_circle([10, 10, 100])
    s.draw_circle_coords(100, 100, 200)

    print(L1)


