angular.module("News")
.controller("NewsController", ["NewsService", function(NewsService) {
  this.newsItems = NewsService.latestNews();
}]);
