def oldTextFinder():
    oldText = []
    if nuke.allNodes('Text'):
        for node in nuke.allNodes():
            node.setSelected(False)
        for node in nuke.allNodes(recurseGroups=True):
            if node.Class() == "Text":
                try:
                    node.setSelected(True)
                    oldText.append(node.name())
                except Exception:
                    pass
        for i in nuke.allNodes('Group'):
            i.begin()
            for node in nuke.allNodes('Text'):
                try:
                    node.setSelected(True)
                    oldText.append(i.name() + " (is a Group node with Text inside)")
                    nodeNames = [n.name() for n in nuke.selectedNodes()]
                    if nodeNames:
                        i.setSelected(True)
                except Exception:
                    pass
            i.end()
        if nuke.ask("<b><center><font color=orange>These are the old Text nodes in your script:\n\n<font color=yellow>" + ', '.join(oldText) + "\n\n<font color=orange>Would you like to zoom on them?"):
            nuke.zoomToFitSelected()
    else:
        nuke.message(
            """<b><center><font color=orange>You don't have any old Text node.\n\n<a href="https://www.gatimedia.co.uk/oldtext2newtext"><font color=yellow><u>Learn about Old vs. New Text\n""")
