angular.module("News")
.factory("NewsService", function() {
  var svc = {};

  svc.latestNews = function() {
    return [
      {
          title: "Category Theory and Declarative Programming",
          postedBy: "CollinsQ",
          postedOn: "11/06/2016",
          url: "http://www.example.com/category-theory",
          points: 4
      },
      {
          title: "What is WebAssembly?",
          postedBy: "papa_bear",
          postedOn: "11/03/2016",
          url: "http://www.example.com/web-assembly",
          points: 2
      },
      {
          title: "How Facebook makes us dumber",
          postedBy: "zebramoss",
          postedOn: "11/08/2016",
          url: "http://www.example.com/dumb-facebook",
          points: 12
      }
    ];
  }

  return svc;
});
