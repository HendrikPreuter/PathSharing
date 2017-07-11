angular.module("myApp.navigation", []).controller("navigationController", function($scope, $http) {
    $scope.token = $http.default.headers.common.Token;
    $scope.id = $scope.token['id'];
    $scope.username = $scope.token['username'];
});