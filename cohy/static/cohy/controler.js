var cohyApp = angular.module('cohyApp', []);

cohyApp.controller('CohyController', function ($scope, $http) {
    $scope.myobjects = [];
    $http.get('/cohy/myobjects').success(function (data) {
        console.log(data)
        console.log('opaaa')
        $scope.myobjects = data

    });
});