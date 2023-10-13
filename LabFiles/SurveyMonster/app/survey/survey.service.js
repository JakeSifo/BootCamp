angular.module("Survey")
.factory("SurveyService", function($http) {
  var svc = {};

  svc.getSurveyQuestions = function(surveyId) {
    return $http.get("/SurveyMonster/app/survey/data.json");
  }

  return svc;
});
