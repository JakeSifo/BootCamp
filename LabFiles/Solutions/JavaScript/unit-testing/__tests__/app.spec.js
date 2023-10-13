
const {returnTrue, principalPlusInterest, throwException} = require('../src/libToTest.js')

describe("Unit Test Suite #1", function () {

   // beforeEach(function () {
   //    console.log("The Unit Test Suite #1 is running ...");
   // });

   it("testing truth and false return values (Unit Test #1)", function () {
      console.log("  Unit Test #1 running... ");
      // expect(returnTrue()).toBeTruthy();
      expect(returnTrue()).not.toBe(false);
   });

   it("testing math (Unit Test #2)", function () {
      var principal = 1000;
      var interest = 5.2;  // %
      console.log("  Unit Test #2 running... ");
      expect(principalPlusInterest(principal, interest)).toEqual(1052);
   });

   it("testing exceptions (Unit Test #3)", function () {
      console.log("  Unit Test #3 running... ");
      expect(function () {
         throwException();
      }).toThrowError("User-defined exception thrown!");
   });

});

describe("Unit Test Suite #2", function() {

   var foo;
   beforeEach(function() {
     foo = {
       callee: function(value) {
         console.log ("Callee called with " + value);
       },
       caller: function (v){
         console.log ("Calling the callee with " + v);
         this.callee(v);
       }
     };
 
     spyOn(foo, 'callee');
     // spyOn(foo, 'callee').and.callThrough();
     foo.caller(555);
   });
 
   it("check if the call has been made", function() {
     expect(foo.callee).toHaveBeenCalled();
   });
 
   it("check a call with parameter(s)", function() {
     expect(foo.callee).toHaveBeenCalledWith(555);
   });
 });
