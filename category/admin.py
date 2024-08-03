from django.contrib import admin
from .models import Category, SubCategory

class CategoryAdmin(admin.ModelAdmin):
    # 리스트에서 보여줄 필드들
    list_display = ('category_id', 'category_name')
    # 리스트에서 검색 가능한 필드
    search_fields = ('category_name',)
    # 필터링 옵션
    list_filter = ('category_name',)

class SubCategoryAdmin(admin.ModelAdmin):
    # 리스트에서 보여줄 필드들
    list_display = ('subCategory_id', 'subCategory_name', 'category')
    # 리스트에서 검색 가능한 필드
    search_fields = ('subCategory_name',)
    # 필터링 옵션
    list_filter = ('category',)
    # 필드 순서 정의 (폼에서의 필드 순서)
    fields = ('subCategory_name', 'category')

# Admin 사이트에 모델 등록
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
