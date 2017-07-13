angular.module("myApp.login", ['ngRoute', 'angular-jwt'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/login', {
            templateUrl: 'Webpages/login/login.html',
            controller: 'loginController'
        });
    }])

    .controller("loginController", ['$scope', '$http', '$location', 'jwtHelper', function($scope, $http, $location, jwtHelper) {
        $scope.token = localStorage.getItem('token');
        if($scope.token != 'undefined' && $scope.token && $scope.token != null) {
            $http.defaults.header.common.Token = $scope.token;
            $location.path('/#!home');
        }

        $scope.login = function(user) {
            if (!user) {
                $scope.error = 'Please enter your username and password';
                return;
            }
            if (!user.username) {
                $scope.error = 'Please enter your username'
                return;
            }
            if (!user.password) {
                $scope.error = 'Please enter your password';
                return;
            }
            var data = {
                "username": user.username,
                "password": user.password
            };
            console.log(data);
            $http.post("http://localhost:5000/login", data).then(function (response) {
                if(response.data.response === 'error') {
                    console.log('error: ', response.data.response);
                    $scope.error = response.data.error;
                } else {
                    console.log('logging in is working');
                    $scope.token = response.data.token;
                    $http.defaults.headers.common.Token = $scope.token;
                    localStorage.setItem('token', $scope.token);
                    window.location.href = '/#!home';
                    location.reload();
                }
            })
        }
    }]);