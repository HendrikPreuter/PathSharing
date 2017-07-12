angular.module("myApp.user", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/user', {
            templateUrl: 'Webpages/user/user.html',
            controller: 'userController'
        });
    }])

    .controller("userController", function($scope, $http) {
        $scope.username = localStorage.getItem('username');
        $scope.userid = localStorage.getItem('userid');

        $scope.signout = function signout(){
            localStorage.clear();
            $http.defaults.headers.common.Token = null;
        };

        $http({
            method: 'GET',
            url: 'http://localhost:5000/user/' + $scope.userid
        }).then(function successCallback(response) {
            $scope.jsVar = response.data;
            console.log(response);
        }, function errorCallback(response) {
            console.log(response);
        })
    });