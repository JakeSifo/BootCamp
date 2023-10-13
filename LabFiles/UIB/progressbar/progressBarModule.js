angular.module('uib.progressbar', ['ui.bootstrap'])
    .controller('ProgressBarCtrl', function ($scope) {

        $scope.charLimit = 20;
        // $scope.charCnt = 0;

        $scope.countChars = function (event) {

            if ($scope.charCnt < $scope.charLimit) {
                $scope.charCnt++;
                
                keyInfo(event);

                if ($scope.charCnt > $scope.charLimit * 0.75) {
                    $scope.progressBarType = 'danger';
                } else if ($scope.charCnt > $scope.charLimit * 0.5) {
                    $scope.progressBarType = 'warning';
                }

            } else {
                console.log("You have reached your verbosity limit for today.")
            }
        }

        function keyInfo(event) {
            console.log("Key with code [" + event.keyCode + "] entered");
            console.log("Key count: " + $scope.charCnt);
        }
    });