def OldText2NewText():
    if nuke.selectedNodes('Text'):
        for oldText in nuke.selectedNodes('Text'):
            ###################
            ## OLD TEXT NODE ##
            ###################
            #NAME
            oldText_name = oldText['name'].value()

            #TEXT
            oldText_output = oldText["output"].value()
            oldText_premult = oldText["premult"].value()
            oldText_cliptype = oldText["cliptype"].value()
            oldText_replace = oldText["replace"].value()
            oldText_invert = oldText["invert"].value()
            oldText_opacity = oldText["opacity"].value()
            oldText_maskChannelMask = oldText["maskChannelMask"].value()
            oldText_maskChannelInput = oldText["maskChannelInput"].value()
            oldText_inject = oldText["inject"].value()
            oldText_invert_mask = oldText["invert_mask"].value()
            oldText_message = oldText["message"].toScript()
            #size - font_size
            oldText_size = oldText["size"].value()
            #kerning - tracking
            oldText_kerning = oldText["kerning"].value()
            oldText_leading = oldText["leading"].value()
            oldText_xjustify = oldText["xjustify"].value()
            oldText_yjustify = oldText["yjustify"].value()
            oldText_box = oldText["box"].value()

            oldText_translate_x = oldText["translate"].value(0)
            oldText_translate_y = oldText["translate"].value(1)
            oldText_rotate = oldText["rotate"].value()
            oldText_scale = oldText["scale"].value()
            oldText_skewX = oldText["skewX"].value()
            oldText_skewY = oldText["skewY"].value()
            oldText_skew_order = oldText["skew_order"].value()
            oldText_center = oldText["center"].value()

            #COLOR
            oldText_ramp = oldText["ramp"].value()
            oldText_color = oldText["color"].value()

            #NODE
            oldText_label = oldText["label"].value()
            oldText_note_font_size = oldText["note_font_size"].value()
            oldText_note_font_color = oldText["note_font_color"].value()
            oldText_hide_input = oldText["hide_input"].value()
            oldText_postage_stamp = oldText["postage_stamp"].value()
            oldText_disable = oldText["disable"].value()

            #DEPENDENCIES
            oldText_dependencies = oldText.dependencies()

            #OLDTEXT DEPENDENTS
            dependents = []
            for node in nuke.allNodes():
                for i in node.dependencies():
                    if i.name() == oldText_name:
                        dependents.append(node.name())

            #POSITION
            oldText_xpos = oldText['xpos'].value()
            oldText_ypos = oldText['ypos'].value()

            nuke.delete(oldText)

            ###################
            ## NEW TEXT NODE ##
            ###################

            newText = nuke.nodes.Text2()

            #NAME
            newText['name'].setValue(oldText_name)

            #POSITION
            newText['xpos'].setValue(oldText_xpos)
            newText['ypos'].setValue(oldText_ypos)

            #DEPENDENCIES
            if oldText_dependencies:
                try:
                    newText.setInput(0, oldText_dependencies[0])
                except Exception:
                    pass

            #RECONNECT DEPENDENTS
            if dependents:
                try:
                    for node in dependents:
                        nuke.toNode(node).setInput(0, newText)
                except Exception:
                    pass

            #TEXT
            newText["output"].setValue(oldText_output)
            newText["premult"].setValue(oldText_premult)
            newText["cliptype"].setValue(oldText_cliptype)
            newText["replace"].setValue(oldText_replace)
            newText["invert"].setValue(oldText_invert)
            newText["opacity"].setValue(oldText_opacity)
            newText["maskChannelMask"].setValue(oldText_maskChannelMask)
            newText["maskChannelInput"].setValue(oldText_maskChannelInput)
            newText["inject"].setValue(oldText_inject)
            newText["invert_mask"].setValue(oldText_invert_mask)
            newText["message"].setValue(oldText_message)
            #size = font_size
            newText["font_size"].setValue(oldText_size)
            newText["global_font_scale"].setValue(0.6)
            #kerning = tracking
            newText["tracking"].setValue(oldText_kerning)
            newText["leading"].setValue(oldText_leading)
            newText["xjustify"].setValue(oldText_xjustify)
            newText["yjustify"].setValue(oldText_yjustify)
            newText["box"].setValue(oldText_box)

            #COLOR
            newText["ramp"].setValue(oldText_ramp)
            newText["color"].setValue(oldText_color)

            #NODE
            newText["label"].setValue(oldText_label)
            newText["note_font_size"].setValue(oldText_note_font_size)
            newText["note_font_color"].setValue(oldText_note_font_color)
            newText["hide_input"].setValue(oldText_hide_input)
            newText["postage_stamp"].setValue(oldText_postage_stamp)
            newText["disable"].setValue(oldText_disable)

            #GROUPS
            newText.showControlPanel()
            animLayers = newText['group_animations'].getAllItems()
            newText['group_animations'].setSelectedItems(animLayers)
            newText["translate"].setValue(oldText_translate_x, 0)
            newText["translate"].setValue(oldText_translate_y, 1)
            newText["rotate"].setValue(oldText_rotate)
            newText["scale"].setValue(oldText_scale)
            newText["skewX"].setValue(oldText_skewX)
            newText["skewY"].setValue(oldText_skewY)
            newText["skew_order"].setValue(oldText_skew_order)
            newText["center"].setValue(oldText_center)
            newText.hideControlPanel()
    else:
        nuke.message("""<center><b><font color=orange>Select some nodes first!\n\n<a href="https://www.gatimedia.co.uk/oldtext2newtext"><font color=yellow><u>Learn about Old vs. New Text\n""")
