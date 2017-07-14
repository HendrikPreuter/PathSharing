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
            } else if(!user.username) {
                $scope.error = "Please fill in your username";
            } else if(!user.email) {
                $scope.error = "Please fill in your email";
            } else if(!user.password) {
                $scope.error = "Please fill in your password";
            } else {
                var data = {
                    'username': user.username,
                    'email': user.email,
                    'password': user.password
                };
                $http.post("http://localhost:5000/user", data).then(function (response) {
                    if (response.data.response === "success") {
                        $scope.success = response.data.success;
                    } else {
                        console.log(response.data.response);
                        $scope.error = response.data.error;
                    }
                })
            }
        };
    });