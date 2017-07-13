angular.module("myApp.signup", ['ngRoute'])
    .config(['$routeProvider', function($routeProvider){
        $routeProvider.when('/signup', {
            templateUrl: 'Webpages/signup/signup.html',
            controller: 'signupController'
        });
    }])

    .controller("signupController", function($scope, $http){
        $scope.signup = function(user) {
            if(!user) {
                console.log("error test");
            } else if(!user.username) {
                console.log("username error");
                $scope.error = "Please fill in your username";
            } else if(!user.email) {
                console.log("email error");
                $scope.error = "Please fill in your email";
            } else if(!user.password) {
                console.log("password error");
                $scope.error = "Please fill in your password";
            } else {
                var data = {
                    'username': user.username,
                    'email': user.email,
                    'password': user.password
                };
                $http.post("http://localhost:5000/user", data).then(function (response) {
                    if (response.data.response === "success") {
                        alert("user created");
                        console.log("succes");
                        window.location.assign('/#!login');
                    } else {
                        console.log(response.data.response);
                        $scope.error = response.data.error;
                    }
                })
            }
        };
    });