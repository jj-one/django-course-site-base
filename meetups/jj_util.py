from django.utils.text import slugify

def before_saving_article(instance, *args, **kwargs):
  # print(f"Check if the model has the target attr: {hasattr(instance, 'slg')}")
  
  if hasattr(instance, 'slug'):
    post_slug = 0
    slug = slugify(instance.title) if not instance.slug else slugify(instance.slug)
    o_slug = slug

    if not hasattr(instance, 'id'):
      similar_slugs = instance.__class__.objects.filter(slug__iexact=slug).count()
      while similar_slugs:
        post_slug += 1
        slug = o_slug + str(post_slug)
        similar_slugs = instance.__class__.objects.filter(slug__iexact=slug).count()
      instance.slug = slug
    else:
      # This is an update
      similar_slugs = instance.__class__.objects.filter(slug__iexact=slug).exclude(id=instance.id).count()
      while similar_slugs:
        post_slug += 1
        slug = o_slug + str(post_slug)
        similar_slugs = instance.__class__.objects.filter(slug__iexact=slug).exclude(id=instance.id).count()
      instance.slug = slug