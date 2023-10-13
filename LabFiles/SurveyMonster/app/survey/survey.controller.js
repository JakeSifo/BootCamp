angular.module("Survey")
.controller("SurveyController", function(SurveyService) {
  this.currentIndex = 0;
  this.questions = [];
  this.currentQuestion = undefined;
  this.submitted = false;

  this.hasNext = function() {
    return this.currentIndex < this.questions.length - 1;
  }

  this.hasPrev = function() {
    return this.currentIndex != 0;
  }

  this.nextQuestion = function() {
    if (this.currentIndex < this.questions.length - 1) {
      this.currentIndex += 1;

      this.currentQuestion = this.questions[this.currentIndex];
    }
  }

  this.prevQuestion = function() {
    if (this.currentIndex > 0) {
      this.currentIndex -= 1;

      this.currentQuestion = this.questions[this.currentIndex];
    }
  }

  this.submitSurvey = function() {
    this.submitted = true;
  }

  this.init = function() {
    var self = this;

    SurveyService.getSurveyQuestions()
      .then(function(response) {
        self.questions = response.data;
        self.currentQuestion = self.questions[0];
      });
  }

  this.init();
});
