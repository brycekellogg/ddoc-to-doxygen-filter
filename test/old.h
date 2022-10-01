




/*******************************
 * Brief description.
 *
 * Detailed description that
 * contains multiple lines. And
 * has multiple sentences.
 *
 * Example:
 * ```
 * OutsideNamespace o = new OutsideNamespace();
 * ```
 *
 *******************************/
class OutsideNamespace {

    /// Tripple slashes count as documentation.
    ///
    /// Here's another detailed description. And
    /// it also has multiple sentences!
    ///
    /// Params:
    ///    val  = a value to pass in!
    ///    name = a string for the name
    ///
    /// Returns: some random int
    ///
    /// Examples:
    /// -------------------
    /// int res = instance.fun1(12, "jim");
    /// ------------------
    int fun1(double val, string name);


    /**
      A breif description for fun1. We
      should support multi-sentence briefs.

      The leading asterisks are not required
      to be counted as a documentation comment.
      That's what this test case is for.

      Params:
          val1 = We also support descriptions
                 of parameters that are
                 multiple lines.
          val2 = but they don't need to be.
      */
    void fun2(int val1, int val2);

    /** Sometimes, you just want a very simple
     *  description. The ending comment delimiter
     *  doesn't need to be on it's own line. */
    void fun3();

    /* This one isn't documented because
     * if doesn't have the correct opening
     * comment delimiter.
     *
     * Note: this should be ignored by the filter!
     */
    void fun4();

    /** single line doc comment */
    void fun5();

    /*!
     * We also support QT style comment blocks.
     *
     * Params:
     *     val1 = a value
     *     val2 = another value
     *
     * Note: This function does somethin
     * Returns: nothing, duh
     */
    void fun6(int val1, int val2);

    //! The QT style for triple slash
    //! also works.
    //!
    //! Example:
    //! --------------
    //! instance.fun7();
    //! --------------
    void fun7();
};



