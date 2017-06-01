var app = angular.module('myApp', []);

app.controller('MyCtrl', ['$scope', function ($scope) {
    $scope.should_display = 'home';
}]);