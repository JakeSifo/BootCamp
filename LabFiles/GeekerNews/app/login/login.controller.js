angular.module("Login")
.controller("LoginController", ["LoginService", function(LoginService) {
  this.email = "";
  this.password = "";
  this.error = "";

  this.login = function() {
    var result = LoginService.authenticate(this.email, this.password);

    if (result == false) {
      this.error = "Login failed.";
    } else {
      this.error = "";
      //Go to news page
      document.location = "/GeekerNews/app/news/index.html";
    }
  }
}]);
