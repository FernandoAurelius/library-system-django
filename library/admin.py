from django.contrib import admin

from library.models import Book, Loan


class ListBooks(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre", "availability")
    list_display_links = ("id", "title")
    list_editable = ("availability",)

class ListLoans(admin.ModelAdmin):
    list_display = ("id", "user", "book", "loan_date", "return_date", "returned")
    list_display_links = ("id",)
    list_editable = ("return_date", "returned")
    search_fields = ("id", "user", "book")
    list_filter = ("return_date",)


admin.site.register(Book, ListBooks)
admin.site.register(Loan, ListLoans)
