/**
 * Created by brend on 11-Jul-17.
 */
/**
 * Created by brend on 11-Jul-17.
 */
angular.module("myApp", []).controller("userController", function($scope, $http) {
    $http({
        method: 'GET',
        url: 'http://localhost:5000/user'
    }).then(function successCallback(response) {
        $scope.jsVar = response.data;
        console.log(response);
    }, function errorCallback(response) {
        console.log(response);
    })
});