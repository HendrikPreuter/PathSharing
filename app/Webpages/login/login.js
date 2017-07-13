angular.module("myApp.login", ['ngRoute', 'angular-jwt'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/login', {
            templateUrl: 'Webpages/login/login.html',
            controller: 'loginController'
        });
    }])

    .controller("loginController", ['$scope', '$http', '$location', 'jwtHelper', function($scope, $http, $location, jwtHelper) {
        $scope.token = localStorage.getItem('token');
        if($scope.token != 'undefined') {
            $http.defaults.header.common.Token = $scope.token;
            $location.path('/#!home');
        }

        $scope.login = function(user) {
            var data = {
                "username": user.username,
                "password": user.password
            };
            console.log(data);
            $http.post("http://localhost:5000/login", data).then(function (response) {
                if(response.data.response === 'error') {
                    console.log(response.data.response);
                    $scope.error = response.data.error;
                } else {
                    $scope.token = response.data.token;
                    $http.defaults.headers.common.Token = $scope.token;
                    localStorage.setItem('token', $scope.token);
                    location.reload();
                    window.location.href = '/#!home';
                }
            })
        }
    }]);