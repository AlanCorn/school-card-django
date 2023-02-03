from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .models import Student  # 引用上一把创建的数据表


class QueryStudent(APIView):
    @staticmethod
    def get(request):
        """
        学生信息获取接口
        """
        req = request.query_params.dict()  # 前端给的json包数据
        try:
            student_id = req["student_id"]
        except KeyError:
            return Response(Student.objects.values())
        else:
            student_info = Student.objects.filter(student_id=student_id).values()
            # student_name = student_info.values("student_name")  # 提取数据表中数据
            return Response(student_info)


class AddStudent(APIView):
    @staticmethod
    def post(request):
        """
        """
        req = request.data  # 前端给的json包数据
        student_id = req["student_id"]
        student_name = req["student_name"]
        student_balance = req["student_balance"]
        Student(student_id=student_id, student_name=student_name, student_balance=student_balance).save()  # 保存数据

        return Response([{'status': 'OK'}])


class CardPay(APIView):
    @staticmethod
    def post(request):
        """
        支付接口
        """
        req = request.data
        student_id = req["student_id"]
        pay_amount = req["pay_amount"]
        try:
            cursor = Student.objects.get(student_id=student_id)
        except ObjectDoesNotExist:
            return Response([{'status': 'Failed', 'message': '学生不存在'}])
        else:
            if cursor.student_balance < pay_amount:
                return Response([{'status': 'Failed', 'message': '余额不足'}])
            else:
                cursor.student_balance -= pay_amount
                cursor.save()
                return Response([{'status': 'OK'}])


class CardCharge(APIView):
    @staticmethod
    def post(request):
        """
        充值接口
        """
        req = request.data
        student_id = req["student_id"]
        charge_amount = req["charge_amount"]
        try:
            cursor = Student.objects.get(student_id=student_id)
        except ObjectDoesNotExist:
            return Response([{'status': 'Failed', 'message': '学生不存在'}])
        else:
            cursor.student_balance += charge_amount
            cursor.save()
            return Response([{'status': 'OK'}])
