from plotly.basedatatypes import BaseLayoutHierarchyType
import copy


class Center(BaseLayoutHierarchyType):

    # lat
    # ---
    @property
    def lat(self):
        """
        Sets the latitude of the map's center. For all projection
        types, the map's latitude center lies at the middle of the
        latitude range by default.
    
        The 'lat' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['lat']

    @lat.setter
    def lat(self, val):
        self['lat'] = val

    # lon
    # ---
    @property
    def lon(self):
        """
        Sets the longitude of the map's center. By default, the map's
        longitude center lies at the middle of the longitude range for
        scoped projection and above `projection.rotation.lon`
        otherwise.
    
        The 'lon' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['lon']

    @lon.setter
    def lon(self, val):
        self['lon'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.geo'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        lat
            Sets the latitude of the map's center. For all
            projection types, the map's latitude center lies at the
            middle of the latitude range by default.
        lon
            Sets the longitude of the map's center. By default, the
            map's longitude center lies at the middle of the
            longitude range for scoped projection and above
            `projection.rotation.lon` otherwise.
        """

    def __init__(self, arg=None, lat=None, lon=None, **kwargs):
        """
        Construct a new Center object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.layout.geo.Center
        lat
            Sets the latitude of the map's center. For all
            projection types, the map's latitude center lies at the
            middle of the latitude range by default.
        lon
            Sets the longitude of the map's center. By default, the
            map's longitude center lies at the middle of the
            longitude range for scoped projection and above
            `projection.rotation.lon` otherwise.

        Returns
        -------
        Center
        """
        super(Center, self).__init__('center')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.layout.geo.Center 
constructor must be a dict or 
an instance of plotly.graph_objs.layout.geo.Center"""
            )

        # Import validators
        # -----------------
        from plotly.validators.layout.geo import (center as v_center)

        # Initialize validators
        # ---------------------
        self._validators['lat'] = v_center.LatValidator()
        self._validators['lon'] = v_center.LonValidator()

        # Populate data dict with properties
        # ----------------------------------
        v = arg.pop('lat', None)
        self.lat = lat if lat is not None else v
        v = arg.pop('lon', None)
        self.lon = lon if lon is not None else v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
