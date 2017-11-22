vmprof it!
----------

These are some unofficial helpers that make using
`vmprof <https://vmprof.readthedocs.io/en/latest/>`_ more pleasant.

For example you can do::

    import vmprofit

    @vmprofit.profile()
    def fn(x):
        do_stuff()


or::

    with vmprofit.profile():
        do_stuff()


``vmprofit.profile`` accepts ``web_url`` and ``auth`` arguments,
by default it uploads profile result of each run to https://vmprof.com
(this **WILL** change in the future to be more explicit).
