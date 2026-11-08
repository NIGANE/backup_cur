from rest_framework import serializers


class SearchSerializer(serializers.Serializer):

    query = serializers.CharField(max_length=255)
    top_k = serializers.IntegerField(default=5, required=False)
    vector = serializers.BooleanField(default=False)
    hybrid = serializers.BooleanField(default=False)
    

    def validate(self, attrs):
        incoming = set(self.initial_data.keys())
        allowed = set(self.fields.keys())
        extra = incoming - allowed
        if extra:
            raise serializers.ValidationError(f"Unexpected fields: {list(extra)}")
        return attrs