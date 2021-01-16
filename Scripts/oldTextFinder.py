def oldTextFinder():
    oldText = []
    if nuke.allNodes('Text'):
        for node in nuke.allNodes():
            node.setSelected(False)
        for node in nuke.allNodes():
            if node.Class() == "Text":
                try:
                    node.setSelected(True)
                    oldText.append(node.name())
                except Exception:
                    pass
        if nuke.ask(
                "<b><center><font color=orange>These are the old Text nodes in your script:\n\n<font color=yellow>" + ', '.join(
                        oldText) + "\n\n<font color=orange>Would you like to zoom on them?"):
            nuke.zoomToFitSelected()
    else:
        nuke.message(
            """<b><center><font color=orange>You don't have any old Text node\n on the root level.\n\n<a href="https://www.gatimedia.co.uk/oldtext2newtext"><font color=yellow><u>Learn about Old vs. New Text\n""")
