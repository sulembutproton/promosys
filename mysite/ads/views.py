from ads.models import Ads
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdsListView(OwnerListView):
    model = Ads
    # By convention:
    # template_name = "ads/article_list.html"


class AdsDetailView(OwnerDetailView):
    model = Ads


class AdsCreateView(OwnerCreateView):
    model = Ads
    fields = ['title', 'text']


class AdsUpdateView(OwnerUpdateView):
    model = Ads
    fields = ['title', 'text']


class AdsDeleteView(OwnerDeleteView):
    model = Ads
