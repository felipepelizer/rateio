from rest_framework import serializers
from .models import Cost_Center


class Cost_Center_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Cost_Center
		fields = "__all__"