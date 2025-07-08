from django.contrib import admin
from .models import Category, Product, ProductImage, Review , Wishlist ,Coupon , OrderItem ,Order



class ProductImageInline(admin.TabularInline): # یا admin.StackedInline
    model = ProductImage
    extra = 1 # تعداد فرم خالی برای آپلود تصویر جدید
   



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # ستون‌هایی که در لیست محصولات نمایش داده می‌شوند
    list_display = ['name', 'category', 'price', 'stock', 'is_active']
    
    # فیلترهایی که در سمت راست صفحه ظاهر می‌شوند
    list_filter = ['category', 'is_active']
    
    # فیلدهایی که مستقیماً از همین لیست قابل ویرایش هستند
    list_editable = ['price', 'stock', 'is_active']
    
    # قابلیت جستجو
    search_fields = ['name', 'description']
    
    # برای ساخت خودکار اسلاگ (slug) از روی نام محصول (اگر فیلد slug دارید)
    prepopulated_fields = {'slug': ('name',)}

    inlines = [ProductImageInline] 
# برای نمایش بهتر دسته‌بندی‌ها، می‌توانید این را هم اضافه کنید
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}




@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'rating', 'created_at')
    search_fields = ('user__username', 'product__name', 'comment')
    list_editable = ('is_approved',)


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display =('user','product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username' , 'product__name')
    autocomplete_fields = ['user' , 'product']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code' , 'valid_from' ,'valid_to' , 'discount' ,'active']
    list_filter = ['active','valid_from','valid_to']
    search_fields = ['code']


class OrderItemInline(admin.TabularInline):
    model = OrderItem 
    rew_id_fields = ['product']
    readonly_fields = ['product','price','quantity']
    extra = 0    #برای جلو گیری از نمایش خالی 



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # ستون‌هایی که در لیست سفارش‌ها نمایش داده می‌شوند
    list_display = ['id', 'user', 'is_paid', 'total_paid', 'created_at']
    
    # فیلترهایی که در سمت راست صفحه ظاهر می‌شوند
    list_filter = ['is_paid', 'created_at']
    
    # قابلیت جستجو بر اساس این فیلدها
    search_fields = ['id', 'user__username']
    
    # اتصال آیتم‌های سفارش به این صفحه
    inlines = [OrderItemInline]

    # برای نمایش بهتر تاریخ‌ها
    date_hierarchy = 'created_at'

