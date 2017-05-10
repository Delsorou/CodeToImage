# -*- coding: utf-8 -*-
"""
    Ron Colorscheme
    ~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter

    Modified by Aaryna Michelle Irwin for CodeToImage
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class RonStyle(Style):

    background_color = '#ffffff'
    styles = {
        Token:              '#00ffff bg:',
        Comment:            '#adff2f',
        Generic.Error:      'bg:',
        Name.Entity:        '#ffff00',
        Comment.Preproc:    '#eea9b8',
        Keyword:            'noinherit #add8e6',
        Generic.Inserted:   'bg:',
        Name.Tag:           'noinherit #add8e6',
        Keyword.Type:       '#2e8b57 nobold',
        Name.Label:         '#eec900',
        Generic.Subheading: '#a9a9a9',
        Generic.Traceback:  '#000000 bg:',
        Name.Variable:      'noinherit #00ffff',
        Generic.Deleted:    'bg:',
        Operator.Word:      '#ff4500',
        Generic.Heading:    '#a9a9a9',
        Name.Constant:      '#00ffff nobold',
        Generic.Output:     '#ffff00 bg:',
    }
