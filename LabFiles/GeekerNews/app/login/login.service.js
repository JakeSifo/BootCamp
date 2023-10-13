angular.module("Login")
.factory("LoginService", function() {
  var svc = {};

  svc.authenticate = function(userId, password) {
    return (userId == "bugs@wb.com" && password == "carrot");
  }

  return svc;
});
