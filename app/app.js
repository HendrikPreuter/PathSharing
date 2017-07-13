angular.module('myApp',
    ['ngRoute',
    'myApp.home',
    'myApp.groups',
    'myApp.about',
    'myApp.signup',
    'myApp.user',
    'myApp.invitations',
    'myApp.login'])
    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/home'});
    }])
    .controller('indexController', ['$scope', '$http', 'jwtHelper', function ($scope, $http, jwtHelper) {
        $scope.token = localStorage.getItem('token');
        if ($scope.token != 'undefined' && $scope.token && $scope.token != null) {
            console.log('scope.token: ', $scope.token);
            $scope.userinfo = jwtHelper.decodeToken($scope.token);
            $scope.username = $scope.userinfo['username'];
            $http.defaults.headers.common.Token = $scope.token;
        }

        $scope.signout = function signout(){
            localStorage.clear();
            $http.defaults.headers.common.Token = null;
            window.location.assign('/#!home');
            location.reload();
        };
    }]);