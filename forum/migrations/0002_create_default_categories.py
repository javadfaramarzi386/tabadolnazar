from django.db import migrations


def create_categories(apps, schema_editor):
    Category = apps.get_model("forum", "Category")

    categories = [

        ("انواع معلولیت", "disabilities", None),

        ("اوتیسم", "autism", "انواع معلولیت"),

        ("سندرم داون", "down-syndrome", "انواع معلولیت"),

        ("سندرم کری دو شا", "cri-du-chat", "انواع معلولیت"),

        ("فلج مغزی", "cerebral-palsy", "انواع معلولیت"),

        ("کم‌توانی ذهنی", "intellectual-disability", "انواع معلولیت"),

        ("اختلال بینایی", "visual-impairment", "انواع معلولیت"),

        ("اختلال شنوایی", "hearing-impairment", "انواع معلولیت"),


        ("درمان", "treatment", None),

        ("کاردرمانی", "occupational-therapy", "درمان"),

        ("گفتاردرمانی", "speech-therapy", "درمان"),

        ("فیزیوتراپی", "physiotherapy", "درمان"),

        ("روانشناسی", "psychology", "درمان"),


        ("آموزش", "education", None),

        ("آموزش در خانه", "home-education", "آموزش"),

        ("مدرسه", "school", "آموزش"),

        ("مهارت های زندگی", "life-skills", "آموزش"),

        ("بازی درمانی", "play-therapy", "آموزش"),

    ]

    created = {}

    order = 1

    for name, slug, parent_name in categories:

        parent = created.get(parent_name)

        obj, _ = Category.objects.get_or_create(
            slug=slug,
            defaults={
                "name": name,
                "parent": parent,
                "display_order": order,
                "is_active": True,
            }
        )

        created[name] = obj

        order += 1


def remove_categories(apps, schema_editor):
    Category = apps.get_model("forum", "Category")

    slugs = [
        "disabilities",
        "autism",
        "down-syndrome",
        "cri-du-chat",
        "cerebral-palsy",
        "intellectual-disability",
        "visual-impairment",
        "hearing-impairment",
        "treatment",
        "occupational-therapy",
        "speech-therapy",
        "physiotherapy",
        "psychology",
        "education",
        "home-education",
        "school",
        "life-skills",
        "play-therapy",
    ]

    Category.objects.filter(slug__in=slugs).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(
            create_categories,
            remove_categories
        ),
    ]