from .models import Category


def forum_categories(request):
    categories = (
        Category.objects.filter(
            is_visible=True,
            is_active=True,
            parent__isnull=True,
        )
        .prefetch_related(
            "children"
        )
        .order_by("display_order", "name")
    )

    return {
        "forum_categories": categories,
    }