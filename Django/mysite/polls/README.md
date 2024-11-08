# Current Progress
Currently attempting to run a test for the Choice model.
intended behaviour:
 - if question doesn't have any Choice optinos (nothing to vote on),
 do no display question.
 - if question has 1 or more Choice options,
 display question in "polls:index"

Currently cannot call "polls:question.id:detail" or "polls:question.id.vote" as
Value after * must be an iterable, not int or question.id (int) is not a set path.

Once can run this test manually in shell, automate it within class "QuestionDetailViewTest".

## Good rules-of-thumb include having:

 - a separate TestClass for each model or view
 - a separate test method for each set of conditions you want to test
 - test method names that describe their function


 A good way to spot untested parts of your application is to check code coverage. This also helps identify fragile or even dead code. If you can’t test a piece of code, it usually means that code should be refactored or removed. Coverage will help to identify dead code. See Integration with coverage.py for details.
