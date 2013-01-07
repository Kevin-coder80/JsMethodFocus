import sublime, sublime_plugin

class JsMethodFocusCommand( sublime_plugin.TextCommand ):

    def run ( self, edit ):
        regions = self.view.sel()
        for region in regions:
            sel = self.view.substr( region )
            self.focus( sel )

    def focus ( self, sel ):
        regions = self.view.find_all( '(function '+ sel +')|((var)? '+ sel +'\s*(=|:)\s*function)' )

        for region in regions:
            word = self.view.substr( region )
            self.view.add_regions( word, [ region ], 'string' )
            self.gotoFocus( word )

    def gotoFocus ( self, word ):
        regions = self.view.get_regions( word )
        self.view.erase_regions( word )

        for region in regions:
            row, _ = self.view.rowcol( region.end() )

        pt = self.view.text_point( row, 0 )
        self.view.sel().clear()
        self.view.sel().add( sublime.Region( pt ) )
        self.view.show( pt )
