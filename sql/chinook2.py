# from here is supposed to be imported Base = declarative_base()
from .schema import *
import numpy as np


class Chinook:
    def __init__(self, fileName):
        addr = "sqlite:///" + fileName
        self._engine = create_engine(addr, echo=False)
        self._sessionMaker = sessionmaker(bind=self._engine)
        Base.metadata.create_all(self._engine)

    def addArtist(self, name):
        with self._sessionMaker() as ses:
            if len(name) > 1:  # this can be avoided
                ids = np.arange(1, len(name), 1)
                for n in name:
                    newartist = Artist(Name=n)
                    ses.add(newartist)
                ses.commit()
                return ids
            else:
                newartist = Artist(Name=name)
                ses.add(newartist)
                ses.commit()
                return newartist.ArtistId

    def getArtist(self, artistId):
        with self._sessionMaker() as ses:
            return ses.query(Artist).where(Artist.ArtistId == artistId).one()

    def allArtists(self):
        with self._sessionMaker() as ses:
            return ses.query(Artist).all()

    def addAlbum(self, title, artistId):
        """ add a single album to the database"""
        with self._sessionMaker() as ses:
            newalbum = Album(Title=title)
            newalbum.ArtistId = artistId
            ses.add(newalbum)
            ses.commit()
            return newalbum.AlbumId

    def addAlbums(self, titles, artistIds):
        """add multiple albums to the database"""
        with self._sessionMaker() as ses:
            for i, tit in enumerate(titles):
                newalbum = Album(Title=tit)
                newalbum.ArtistId = artistIds[i]
                ses.add(newalbum)
            ses.commit()
            return("all good!")

    def getAlbum(self, albumId):
        """find a single album from his id"""
        with self._sessionMaker() as ses:
            return ses.query(Album).where(Album.AlbumId == albumId).one()

    def allAlbums(self):
        """return all the albums in the database"""
        with self._sessionMaker() as ses:
            return ses.query(Album).all()

    def addTrack(self, name, albumId, length):
        with self._sessionMaker() as ses:
            newtrack = Track(Name=name)
            newtrack.AlbumId = albumId
            newtrack.Length = length
            ses.add(newtrack)
            ses.commit()
            return newtrack.TrackId

    def getTrack(self, trackId):
        with self._sessionMaker() as ses:
            return ses.query(Track).where(Track.TrackId == trackId).one()

    def allTracks(self):
        with self._sessionMaker() as ses:
            return ses.query(Track).all()
